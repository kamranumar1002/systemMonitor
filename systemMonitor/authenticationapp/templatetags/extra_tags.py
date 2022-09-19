# This is a file to register extra filters that are not builtin in Django but they are needed in your application

from django import template
from authenticationapp.models import TblBenchmark, TblClients, TblSites, TblSystem


register = template.Library()

# This is a method to split process and remove the 'ram' or 'cpu' written at the end of process name
@register.filter(name='split')
def split(value):
    process_name = value.split(' ')[:-1]
    # converting process name list to string
    return "".join(process_name)

# This is a method to split process and remove the 'used written at the end of drive name
@register.filter(name='split2')
def split2(value):
    drive_name = value.split('_')[:-1]
    # converting process name list to string
    return " ".join(drive_name)


# This method is to return only hour and minute from the whole datetime
@register.filter(name='timedelta')
def timedeltaa(value):
    year, month, day, hour, min, zone = value.strftime("%Y %m %d %I %M %p").split()
    time_hour_minute = (f"{hour}:{min} {zone}")
    return time_hour_minute

# This method is to return site name from site_id
@register.filter(name='site')
def site(value):
    site_name = TblSites.objects.get(site_id = value).site_name
    return site_name

# This method is to return system name from system_id
@register.filter(name='system')
def system(value):
    system_name = TblSystem.objects.get(system_id = value).system_name
    return system_name

# This method is to return client name from client_id
@register.filter(name='client')
def client(value):
    client_name = TblClients.objects.get(client_id = value).client_name
    return client_name

# This method is to return benchhmark name from bnc_id
@register.filter(name='benchmark')
def benchmark(value):
    benchmark_name = TblBenchmark.objects.get(bnc_id = value).bnc_process
    return benchmark_name

# This method is to return process name if it has ram at the end, from bnc_id
@register.filter(name='top_ram')
def top_ram(value):
    top_ram_name = TblBenchmark.objects.get(bnc_id = value).bnc_process
    if top_ram_name[-3:] == "ram":
        return True
    else:
        return False

# This method is to return process name if it has cpu at the end, from bnc_id
@register.filter(name='top_cpu')
def top_cpu(value):
    top_cpu_name = TblBenchmark.objects.get(bnc_id = value).bnc_process
    if top_cpu_name[-3:] == "cpu":
        return True
    else:
        return False

# This method is to return process name if it has drive at the start, from bnc_id
@register.filter(name='drive')
def drive(value):
    drive = TblBenchmark.objects.get(bnc_id = value).bnc_process
    if drive[:5] == "Drive":
        return True
    else:
        return False
        


