from multiprocessing import Event
import site
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import TblBenchmark, TblClients, TblSites, TblSystem, TblEvent
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage


# Create your views here.

def loginUser(request):
    # redirecting to dashboard if user is logged in
    if request.user.is_authenticated:
        return redirect('/')

    # authenticating user if he submitted login form 
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # redirecting to dashboard if user credidentials are legit
            return redirect('/')
        else:
            # Showing alert message if credidentials are wrong
            messages.info(request, 'Incorrect username or password')
            return redirect('/login')
    return render(request, 'login.html')


def logoutUser(request):
    # logging user out
    logout(request)
    messages.info(request, 'Logout successful')
    # redirecting user to login page after he logged out
    return redirect('/login')

@login_required(redirect_field_name='login-to-continue', login_url="/login")
def index(request):
    # getting all the events and ordering them by latest
    events = TblEvent.objects.all().order_by('-event_creation_date')
    # getting all entries in benchmark table
    benchmark = TblBenchmark.objects.all()
    # getting all entries in system table
    systems = TblSystem.objects.all()
    # pagination
    paginator = Paginator(events, 15)
    page = request.GET.get('page')
    try:
        events = paginator.get_page(page)
    except PageNotAnInteger:
        page = 1
        events = paginator.get_page(page)
    except EmptyPage:
        page = paginator.num_pages
        events = paginator.get_page(page)

    # defining context dictionary
    context = {'events':events,'benchmark':benchmark, 'systems':systems, 'paginator':paginator}

    return render(request, "index.html", context )
    

@login_required(redirect_field_name='login-to-continue', login_url="/login")
def viewClients(request):
    # getting all entries in clients table
    clients = TblClients.objects.all()
    # pagination
    paginator = Paginator(clients, 15)
    page = request.GET.get('page')
    try:
        clients = paginator.get_page(page)
    except PageNotAnInteger:
        page = 1
        clients = paginator.get_page(page)
    except EmptyPage:
        page = paginator.num_pages
        clients = paginator.get_page(page)
    # defining context dictionary
    context = {'clients': clients, 'paginator':paginator}


    return render(request, "clients.html", context)


# This view is for getting sites only for selected Client
@login_required(redirect_field_name='login-to-continue', login_url="/login")
def viewSites(request, id):
    # getting all sites for the selected client
    sites = TblSites.objects.all().filter(client_id=id)
        # getting all entries in clients table
    clients = TblClients.objects.all()
    # pagination
    paginator = Paginator(sites, 15)
    page = request.GET.get('page')
    try:
        sites = paginator.get_page(page)
    except PageNotAnInteger:
        page = 1
        sites = paginator.get_page(page)
    except EmptyPage:
        page = paginator.num_pages
        sites = paginator.get_page(page)
    # defining context dictionary
    context = {'sites': sites, 'clients':clients, 'paginator':paginator}

    return render(request, "sites.html", context)


# This view is for getting all sites
@login_required(redirect_field_name='login-to-continue', login_url="/login")
def viewAllSites(request):
    # getting all entries in sites table
    sites = TblSites.objects.all()
    # getting all entries in clients table
    clients = TblClients.objects.all()
    # pagination
    paginator = Paginator(sites, 15)
    page = request.GET.get('page')
    try:
        sites = paginator.get_page(page)
    except PageNotAnInteger:
        page = 1
        sites = paginator.get_page(page)
    except EmptyPage:
        page = paginator.num_pages
        sites = paginator.get_page(page)
    # defining context dictionary
    context = {'sites': sites, 'clients':clients, 'paginator':paginator}

    return render(request, "sites.html", context)

# This view is for getting Systems only for selected Site
@login_required(redirect_field_name='login-to-continue', login_url="/login")
def viewSystems(request, id):
    # getting all systems for the selected site
    systems = TblSystem.objects.all().filter(site_id=id)
    # getting all entries in sites table
    sites = TblSites.objects.all()
    # pagination
    paginator = Paginator(systems, 15)
    page = request.GET.get('page')
    try:
        systems = paginator.get_page(page)
    except PageNotAnInteger:
        page = 1
        systems = paginator.get_page(page)
    except EmptyPage:
        page = paginator.num_pages
        systems = paginator.get_page(page)
    # defining context dictionary
    context = {'systems': systems, 'sites':sites, 'paginator':paginator}

    return render(request, "systems.html", context)


# This view is for getting all systems
@login_required(redirect_field_name='login-to-continue', login_url="/login")
def viewAllSystems(request):
    # getting all entries in systems table
    systems = TblSystem.objects.all()
    # getting all entries in sites table
    sites = TblSites.objects.all()
    # pagination
    paginator = Paginator(systems, 15)
    page = request.GET.get('page')
    try:
        systems = paginator.get_page(page)
    except PageNotAnInteger:
        page = 1
        systems = paginator.get_page(page)
    except EmptyPage:
        page = paginator.num_pages
        systems = paginator.get_page(page)
    # defining context dictionary
    context = {'systems': systems, 'sites':sites, 'paginator':paginator}

    return render(request, "systems.html", context)


@login_required(redirect_field_name='login-to-continue', login_url="/login")
def systemDetail(request, id):
    # getting time 45 minutes earlier than current time
    time = datetime.now() - timedelta(minutes=45)

    # getting entries in events table of the specified system from last 45 minutes ordering by latest 
    events = TblEvent.objects.all().filter(event_creation_date__gte=time, system_id=id).order_by('-event_creation_date')

    # getting all entries in benchmark table
    benchmark = TblBenchmark.objects.all()
    # getting system name
    system = TblSystem.objects.get(system_id = id).system_name

    # Getting benchmark id of average ram value 
    average_ram_bnc_id = TblBenchmark.objects.get(bnc_process="average_ram_value").bnc_id

    # Getting benchmark id of average cpu value 
    average_cpu_bnc_id = TblBenchmark.objects.get(bnc_process="average_cpu_value").bnc_id

    try:
        # getting latest entry of average ram value
        ram_value = TblEvent.objects.all().filter(bnc_id=average_ram_bnc_id, system_id = id).order_by('-event_creation_date')[0].event_value

        # getting latest entry of average cpu value
        cpu_value = TblEvent.objects.all().filter(bnc_id=average_cpu_bnc_id, system_id = id).order_by('-event_creation_date')[0].event_value
    except IndexError:
        ram_value = ""
        cpu_value = ""

    #getting latest 5 entries for average ram value to be displsyed on graph
    average_ram_graph = TblEvent.objects.all().filter(system_id=id, bnc_id=average_ram_bnc_id).order_by('-event_creation_date')[::-1][:5]
    
    #getting latest 5 entries for average cpu value to be displsyed on graph
    average_cpu_graph = TblEvent.objects.all().filter(system_id=id, bnc_id=average_cpu_bnc_id).order_by('-event_creation_date')[::-1][:5]


    # defining context dictionary
    context = {'benchmark': benchmark, 'events':events, 'average_ram_graph':average_ram_graph,'average_cpu_graph':average_cpu_graph, 'system':system, 'ram_value':ram_value, 'cpu_value':cpu_value}

    return render(request, "system-detail.html", context)

# view for search feature in systems page
def searchSystems(request):
    search = request.GET['search']
    systems = TblSystem.objects.filter(system_name__icontains=search)
    sites = TblSites.objects.all()
    context = {'systems':systems, 'sites':sites}
    return render(request, 'systems.html', context)

# view for search feature in sites page
def searchSites(request):
    
    search = request.GET['search']
    sites = TblSites.objects.filter(site_name__icontains=search)
    systems = TblSystem.objects.all()
    context = {'sites':sites, 'systems':systems}
    return render(request, 'sites.html', context)


# view for search feature in clients page
def searchClients(request):
    
    search = request.GET['search']
    clients = TblClients.objects.filter(client_name__icontains=search)
    context = {'clients':clients}
    return render(request, 'clients.html', context)


# view for search feature in dashboard page
def searchDashboard(request):
    
    search = request.GET['search']
    benchmark = TblBenchmark.objects.filter(bnc_process__icontains=search)
    events = TblEvent.objects.all()
    systems = TblSystem.objects.all()
    context = {'events':events, 'benchmark':benchmark, 'systems':systems}
    return render(request, 'search.html', context)
