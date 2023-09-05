from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Recipe, Comment
from .forms import CommentForm


class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 8


class RecipeDetail(View):
    def get(self, request, slug, comment_id=None, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.all().order_by("created_on")
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_to_edit = None
        if comment_id:
            comment_to_edit = get_object_or_404(Comment, id=comment_id)
            comment_form = CommentForm(instance=comment_to_edit)
            comment_form.fields["body"].label = "Edit your comment here:"
        else:
            comment_form = CommentForm()

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": comment_form,
                "editing_comment": comment_to_edit,
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.all().order_by("created_on")
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        if "delete_comment_id" in request.POST:
            comment_id = request.POST.get("delete_comment_id")
            comment_to_delete = get_object_or_404(Comment, id=comment_id)
            if comment_to_delete.name == request.user.username:
                comment_to_delete.delete()
                return HttpResponseRedirect(
                    reverse("recipe_detail", args=[slug])
                )

        elif "editing_comment_id" in request.POST:
            comment_id = request.POST.get("editing_comment_id")
            comment_to_edit = get_object_or_404(Comment, id=comment_id)
            comment_form = CommentForm(request.POST, instance=comment_to_edit)
            if (
                comment_form.is_valid()
                and comment_to_edit.name == request.user.username
            ):
                comment_form.save()
                return HttpResponseRedirect(
                    reverse("recipe_detail", args=[slug])
                )

        else:
            comment_form = CommentForm(data=request.POST)
            if comment_form.is_valid():
                comment_form.instance.name = request.user.username
                comment = comment_form.save(commit=False)
                comment.recipe = recipe
                comment.save()

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked,
            },
        )


class RecipeLike(View):
    def post(self, request, slug, *args, **kwargs):
        recipe = get_object_or_404(Recipe, slug=slug)
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.likes.remove(request.user)
        else:
            recipe.likes.add(request.user)
        return HttpResponseRedirect(reverse("recipe_detail", args=[slug]))


def recipe_detail_delete_comment(request, slug, comment_id):
    if request.method == "POST":
        comment = Comment.objects.get(id=comment_id)
        if comment.name == request.user.username:
            comment.delete()
            return HttpResponseRedirect(reverse("recipe_detail", args=[slug]))
