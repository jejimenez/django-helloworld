from django.forms import ModelForm 
from .models import Job
from crispy_forms.helper import FormHelper
from djangular.forms import NgModelFormMixin#NgFormValidationMixin, NgModelFormMixin, AddPlaceholderFormMixin


class JobForm(NgModelFormMixin, ModelForm):
    """
    Job Form with a little crispy forms added! 
    """
    def __init__(self, *args, **kwargs):
        super(JobForm, self).__init__(*args, **kwargs)
        setup_bootstrap_helpers(self)
        for field in self:
            field.field.widget.attrs.update({'ng-focus': ''})
            field.field.widget.attrs.update({'ng-model': format(field.name),'get-error-elements': '',
        })

    class Meta:
        model = Job
        fields = ('name', 'description',)

def setup_bootstrap_helpers(object):
    object.helper = FormHelper()
    object.helper.form_class = 'form-horizontal'
    object.helper.label_class = 'col-lg-3'
    object.helper.field_class = 'col-lg-8'