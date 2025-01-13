from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from kitchen.forms import (
    DishForm,
    CookForm,
    DishTypeForm,
    CookUpdateForm,
    DishNameSearchForm,
    CookUsernameSearchForm,
    DishTypeNameSearchForm,
    IngredientForm,
    IngredientNameSearchForm
)
from kitchen.models import Dish, Cook, DishType, Ingredient


def index(request: HttpRequest) -> HttpResponse:
    num_of_dishes = Dish.objects.count()
    num_of_cooks = Cook.objects.count()
    num_of_dish_types = DishType.objects.count()
    num_of_ingredients = Ingredient.objects.count()
    num_of_visits = request.session.get("num_of_visits", 0)
    request.session["num_of_visits"] = num_of_visits + 1

    context = {
        "num_of_dishes": num_of_dishes,
        "num_of_cooks": num_of_cooks,
        "num_of_dish_types": num_of_dish_types,
        "num_of_ingredients": num_of_ingredients,
        "num_of_visits": num_of_visits + 1,
    }
    return render(request, "kitchen/index.html", context=context)


class DishListView(LoginRequiredMixin, generic.ListView):
    model = Dish
    paginate_by = 5
    queryset = Dish.objects.select_related("dish_type")

    def get_context_data(self, **kwargs):
        context = super(DishListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = DishNameSearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        form = DishNameSearchForm(self.request.GET)

        if form.is_valid():
            queryset = queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )
        return queryset


class DishCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    form_class = DishForm
    success_url = reverse_lazy("kitchen:dish-list")


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish


class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    form_class = DishForm

    def get_success_url(self):
        return reverse_lazy("kitchen:dish-detail", kwargs={"pk": self.object.pk})


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    success_url = reverse_lazy("kitchen:dish-list")
    template_name = "kitchen/dish_confirm_delete.html"


class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook
    paginate_by = 5
    queryset = Cook.objects.prefetch_related("dishes")

    def get_context_data(self, **kwargs):
        context = super(CookListView, self).get_context_data(**kwargs)
        username = self.request.GET.get("username", "")
        context["search_form"] = CookUsernameSearchForm(
            initial={"username": username}
        )
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        form = CookUsernameSearchForm(self.request.GET)
        if form.is_valid():
            queryset = queryset.filter(
                username__icontains=form.cleaned_data["username"]
            )
            return queryset


class CookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Cook
    form_class = CookForm
    success_url = reverse_lazy("kitchen:cook-list")


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook


class CookUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Cook
    form_class = CookUpdateForm

    def get_success_url(self):
        return reverse_lazy("kitchen:cook-detail", kwargs={"pk": self.object.pk})


class CookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Cook
    success_url = reverse_lazy("kitchen:cook-list")
    template_name = "kitchen/cook_confirm_delete.html"


class DishTypeListView(LoginRequiredMixin, generic.ListView):
    model = DishType
    context_object_name = "dish_type_list"
    template_name = "kitchen/dish_type_list.html"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(DishTypeListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = DishTypeNameSearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        form = DishTypeNameSearchForm(self.request.GET)
        if form.is_valid():
            queryset = queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )
            return queryset


class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    form_class = DishTypeForm
    success_url = reverse_lazy("kitchen:dish-type-list")
    template_name = "kitchen/dish_type_form.html"
    context_object_name = "dish_type"


class DishTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DishType
    success_url = reverse_lazy("kitchen:dish-type-list")
    template_name = "kitchen/dish_type_confirm_delete.html"
    context_object_name = "dish_type"


class DishTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DishType
    form_class = DishTypeForm
    template_name = "kitchen/dish_type_form.html"
    context_object_name = "dish_type"

    def get_success_url(self):
        return reverse_lazy("kitchen:dish-type-detail", kwargs={"pk": self.object.pk})


class DishTypeDetailView(LoginRequiredMixin, generic.DetailView):
    model = DishType
    context_object_name = "dish_type"
    template_name = "kitchen/dish_type_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["dishes"] = Dish.objects.filter(dish_type=self.object)
        return context


class IngredientCreateView(LoginRequiredMixin, generic.CreateView):
    model = Ingredient
    form_class = IngredientForm
    success_url = reverse_lazy("kitchen:ingredient-list")


class IngredientListView(LoginRequiredMixin, generic.ListView):
    model = Ingredient
    paginate_by = 25
    template_name = "kitchen/ingredient_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        name = self.request.GET.get("name", "")
        context["search_form"] = IngredientNameSearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        form = IngredientNameSearchForm(self.request.GET)
        if form.is_valid():
            queryset = queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )
            return queryset


class IngredientDetailView(LoginRequiredMixin, generic.DetailView):
    model = Ingredient


@login_required
def toggle_assign_to_dish(request: HttpRequest, pk) -> HttpResponse:
    cook = Cook.objects.get(id=request.user.id)
    if Dish.objects.get(id=pk) in cook.dishes.all():
        cook.dishes.remove(pk)
    else:
        cook.dishes.add(pk)
    return HttpResponseRedirect(reverse_lazy("kitchen:dish-detail", kwargs={"pk": pk}))
