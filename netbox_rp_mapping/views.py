from netbox.views import generic
from . import forms, models, tables


class RPView(generic.ObjectView):
    queryset = models.StaticRP.objects.all()

    def get_extra_context(self, request, instance):
        table = tables.GroupTable(instance.mcast_rp.all())
        table.configure(request)
        return {"rules_table": table}


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
