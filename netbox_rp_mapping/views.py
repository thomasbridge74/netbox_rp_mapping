from netbox.views import generic
from . import forms, models, tables


class RPView(generic.ObjectView):
    queryset = models.StaticRP.objects.all()


class RPListView(generic.ObjectListView):
    queryset = models.StaticRP.objects.all()
    table = tables.RPTable


class RPEditView(generic.ObjectEditView):
    queryset = models.StaticRP.objects.all()
    form = forms.RPForm


class RPDeleteView(generic.ObjectDeleteView):
    queryset = models.StaticRP.objects.all()


class RPGroupView(generic.ObjectView):
    queryset = models.RPGroupEntry.objects.all()


class RPGroupListView(generic.ObjectListView):
    queryset = models.RPGroupEntry.objects.all()
    table = tables.GroupTable


class RPGroupEditView(generic.ObjectEditView):
    queryset = models.RPGroupEntry.objects.all()
    form = forms.RPGroupEntry


class RPGroupDeleteView(generic.ObjectDeleteView):
    queryset = models.RPGroupEntry.objects.all()
