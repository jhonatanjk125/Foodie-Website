from django.shortcuts import get_object_or_404, redirect, render
from accounts.views import check_vendor_role
from .forms import VendorForm
from accounts.forms import UserProfileForm
from accounts.models import UserProfile
from .models import Vendor
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from menu.models import Category


# Create your views here.
@login_required(login_url='login')
@user_passes_test(check_vendor_role)
def vendorProfile(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    vendor = get_object_or_404(Vendor, user=request.user)
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, request.FILES, instance=profile)
        vendor_form = VendorForm(request.POST, request.FILES, instance=vendor)
        if profile_form.is_valid() and vendor_form.is_valid():
            profile_form.save()
            vendor_form.save()
            messages.success(request, 'Information updated')
            return redirect('vendorProfile')
        else:
            pass
    else:
        profile_form = UserProfileForm(instance=profile)
        vendor_form = VendorForm(instance=vendor)
    
    context = {
        'profile_form': profile_form,
        'vendor_form': vendor_form,
        'profile': profile,
        'vendor': vendor,
    }
    return render(request, 'vendor/vendorProfile.html', context)


def menuBuilder(request):
    vendor = Vendor.objects.get(user=request.user)
    categories = Category.objects.filter(vendor=vendor)
    context = {
        'categories': categories,
    }
    return render(request, 'vendor/menuBuilder.html', context)
