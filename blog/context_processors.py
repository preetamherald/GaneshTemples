from django.utils import timezone
from blog.models import Post

def add_variable_to_context(request):
    recents = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:2]
    highlights = Post.objects.filter(published_date__lte=timezone.now()).order_by('-likes')[:2]
    return {
        'recents': recents,
        'highlights': highlights,
    }