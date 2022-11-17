from rest_framework.viewsets import ModelViewSet

from core.models import Autor, Categoria, Editora, Livro, Usuario
from core.serializers import (
    AutorSerializer,
    CategoriaSerializer,
    EditoraSerializer,
    LivroDetailSerializer,
    LivroSerializer,
)
