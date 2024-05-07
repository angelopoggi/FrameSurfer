from django import forms

class TopcisForm(forms.Form):
    OPTIONS = (
        ('option1', 'Option 1'),
        ('option2', 'Option 2'),
        ('option3', 'Option 3'),
    )

    my_choices = forms.MultipleChoiceField(
        choices=OPTIONS,
        widget=forms.CheckboxSelectMultiple,
        label="Select Options",
    )
    matt_choices = [
        ("none", None),
        ("shadowbox", "shadowbox")
    ]
    matt_choice = models.CharField(choices=matt_choices)
