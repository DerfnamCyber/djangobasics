from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    title           = forms.CharField(label='', widget = forms.TextInput(attrs={'placeholder' : "Your Title"})) 
    description     = forms.CharField(
                        required=False,
                        widget = forms.Textarea(
                            attrs={
                                'class' : 'new-class-name two',
                                'id' : 'my-id-for-textarea',
                                'rows' : 20,
                                'cols' : 120,
                            }
                        )
                        
                    )
    price           = forms.DecimalField()
             
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

    # def clean_title(self, *args, **kwargs):
    #     title = self.cleaned_data.get("title")
    #     if "cfe" in title:
    #         return title
    #     else:
    #         raise forms.ValidationError("This is not a valid title")     
    #     return 
    


class RawProductForm(forms.Form):
    title           = forms.CharField(label='', widget = forms.Textarea(attrs={'placeholder' : "Your Title"}))
    description     = forms.CharField(
                        required=False,
                        widget = forms.Textarea(
                            attrs={
                                'class' : 'new-class-name two',
                                'id' : 'my-id-for-textarea',
                                'rows' : 20,
                                'cols' : 120,
                            }
                        )
                        
                    )
    price           = forms.DecimalField()