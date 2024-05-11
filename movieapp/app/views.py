from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from app.models import Movie
from app.forms import movieform
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
# def home(request):
#     m=Movie.objects.all()
#     return render(request,'home.html',{'m':m})

class HomeView(ListView):
    model=Movie
    template_name="home.html"
    context_object_name='m'
    #queryset=Movie.objects.filter(year=2024)
    # def get_queryset(self):
    #     queryset=self.get_queryset().filter(year=2023)
    #     return queryset
    # def get(self,request):
    #     m = Movie.objects.all()
    #     return render(request,'home.html',{'m':m})





# def detail(request,n):
#     m=Movie.objects.get(id=n)
#     return render(request, 'detail.html', {'m': m})

class Detail(DetailView):
    model=Movie
    template_name="detail.html"
    context_object_name="m"


# def addmovie(request):
#     if(request.method=="POST"):
#         form=movieform(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#             return home(request)
#
#
#     form=movieform() #Empty form object
#
#     return render(request,'add.html',{'form':form})

class AddMovie(CreateView):
    def get(self,request):
        form = movieform()  # Empty form object

        return render(request,'add.html',{'form':form})
    def post(self,request):
        form = movieform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('app:home')


# class AddMovie(CreateView):
#     model=Movie
#     template_name="add.html"
#     fields=['name','year','desc','image']
#     success_url=reverse_lazy('app:home')

class Update(UpdateView):
    model=Movie
    template_name = "add.html"
    fields = ['name', 'year', 'desc', 'image']
    success_url = reverse_lazy('app:home')

# def update(request,n):
#     m=Movie.objects.get(id=n)
#     if(request.method=="POST"):
#         form=movieform(request.POST,request.FILES,instance=m)
#         if form.is_valid():
#             form.save()
#             return home(request)
#
#
#     form=movieform(instance=m) #Empty form object
#
#     return render(request,'add.html',{'form':form})


# def delete(request,n):
#     m = Movie.objects.get(id=n)
#     m.delete()
#     return reverse_lazy('app:home')

class Delete(DeleteView):
    model=Movie
    template_name="delete.html"
    success_url = reverse_lazy('app:home')









