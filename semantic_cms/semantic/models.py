#Semantic models

# from django.db import models
#
# class Semantic(models.Model):
#     """
#     Semantic is some kind of category. Every Article can has one or more Semantic category.
#     """
#
#     name = models.CharField(max_length=128, unique=True)
#
#     relationships = models.ManyToManyField("self", through="Relationship",blank=True, symmetrical=False, related_name="related_to")
#
#     edited_date = models.DateTimeField('date edited', null=True, blank=True)
#     created_date = models.DateTimeField('date created')
#
#     def __str__(self):
#         return self.name
#
# class Relationship(models.Model):
#     parent = models.ForeignKey(Semantic, related_name="parents")
#     child = models.ForeignKey(Semantic, related_name="childs")
#
#     def __str__(self):
#         return self.parent.name + " -> " + self.child.name


from django.db import models
from django_dag.models import *
from django.utils import timezone
from django.utils.text import slugify

class Semantic(node_factory('semantic.SemanticEdge')):
    """
    Semantic is some kind of category. Every Article can has one or more Semantic category.
    """

    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(max_length=50, unique=True, blank=True,  null=True)

    # relationships = models.ManyToManyField("self", through="Relationship",blank=True, symmetrical=False, related_name="related_to")

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """Override save"""
        if (self.slug != slugify(self.name)):
            print("-----DEBUG----")
            print(self.slug)
            print(slugify(self.name))
            print("-------------")
            self.slug = slugify(self.name)


        super(Semantic, self).save(*args, **kwargs)

    def type(self):
        return "semantic"


class SemanticEdge(edge_factory('semantic.Semantic', concrete = False)):
    """
    SemanticEdge model class
    """

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.parent.name + " -> " + self.child.name

    def parentId(self):
        return self.parent.id

    def childId(self):
        return self.child.id

    def parentSlug(self):
        return self.parent.slug

    def childSlug(self):
        return self.child.slug

    # def save(self, *args, **kwargs):
    #     """Override save"""
    #     time = timezone.now()
    #     self.created_date = time
    #
    #     super(SemanticEdge, self).save(*args, **kwargs)
