from django.contrib import admin
import inspect
import api.models as models
from django.db.models.base import ModelBase

#Register ALL models
for model_name in dir(models):
    model = getattr(models, model_name)
    if isinstance(model, ModelBase) and  not(model._meta.abstract) and model_name!="User":
        admin.site.register(model)
