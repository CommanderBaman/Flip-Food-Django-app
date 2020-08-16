from django.shortcuts import render

from .models import Food

# handling the display of the food objects
from django.views.generic import ( 
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView, 
    DeleteView   
)

# to add the login required condition on classes
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# main page of the food delivery system
class FoodListView( ListView):
    model = Food
    template_name = 'food_delivery/main.html'
    context_object_name = 'foods'
    ordering = ['-datePosted']
    paginate_by = 4

    def get_context_data( self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['foodInfos'] = self.request.user.cart.foodinfo_set.all()
            context['noFoods'] = False
        except:
            context['noFoods'] = True
        return context

# see details of a single food object
class FoodDetailView( DetailView):
    model = Food
    template_name = 'food_delivery/food-detail.html'
    context_object_name = 'food'

# to create a new food object
class FoodCreateView( LoginRequiredMixin, CreateView):
    model = Food
    template_name = 'food_delivery/food-create.html'
    context_object_name = 'food'

    fields = ['name', 'description', 'quantity', 'ingredients', 'price', 'discount', 'image']

    def form_valid( self, form):
        form.instance.author = self.request.user
        return super().form_valid( form)
    

# to update the food object details
class FoodUpdateView( LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Food
    template_name = 'food_delivery/food-create.html'
    context_object_name = 'food'

    fields = ['name', 'description', 'quantity', 'ingredients', 'price', 'discount', 'image']

    def form_valid( self, form):
        form.instance.author = self.request.user
        return super().form_valid( form)
    
    def test_func( self):
        fooder = self.get_object()
        
        # to avoid updates by other persons
        if self.request.user == fooder.seller:
            return True
        return False

# to delete the food object
class FoodDeleteView( LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Food
    template_name = 'food_delivery/food-delete.html'
    context_object_name = 'food'

    # sending to home page 
    success_url = '/'

    def test_func( self):
        fooder = self.get_object()
        
        # to avoid updates by other persons
        if self.request.user == fooder.seller:
            return True
        return False
    

# shows the about us page
def about( request):
    context = {}
    return render( request, 'food_delivery/about.html', context)

