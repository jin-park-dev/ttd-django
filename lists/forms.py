from django import forms
from django.core.exceptions import ValidationError

from lists.models import Item

# class ItemForm(forms.Form):
#     item_text = forms.CharField(
#         widget=forms.fields.TextInput(attrs={
#             'placeholder': 'Enter a to-do item',
#             'class': 'form-control input-lg',
#         }),
#     )

EMPTY_ITEM_ERROR = "You can't have am empty list item"
DUPLICATE_ITEM_ERROR = "You've already got this in your list"    


class ItemForm(forms.models.ModelForm):

    class Meta:
        model = Item
        fields = ('text',)
        widgets = {
            'text': forms.fields.TextInput(attrs={
                'placeholder': 'Enter a to-do item',
                'class': 'form-control input-lg',
            }),
        }
        error_messages = {
            'text': {'required': EMPTY_ITEM_ERROR}
        }

    def save(self, for_list):
        self.instance.list = for_list
        return super().save()


# self.instance is model class
class ExistingListItemForm(ItemForm):
    
    def __init__(self, for_list, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance.list = for_list

#That’s a bit of Django voodoo right there, but we basically take the validation error, adjust its error message, and then pass it back into the form.
    def validate_unique(self):
        try:
            self.instance.validate_unique()
        except ValidationError as e:
            e.error_dict = {'text': [DUPLICATE_ITEM_ERROR]}
            self._update_errors(e)
            
    # Personal opinion here: I could have used super, but I prefer not to use super when it requires arguments, say, to get a grandparent method. I find Python 3’s super() with no args awesome to get the immediate parent. Anything else is too error-prone, and I find it ugly besides. YMMV. 
    def save(self):
        return forms.models.ModelForm.save(self)
