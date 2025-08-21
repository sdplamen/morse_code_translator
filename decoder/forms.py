from django import forms
from decoder.models import MorseMapping
class MorseMappingForm(forms.ModelForm):
    class Meta:
        model = MorseMapping
        fields = ['morse_code', 'character']
        labels = {
            'morse_code': 'Morse Code Sequence',
            'character': 'Character (A-Z, 0-9)',
        }
        help_texts = {
            'morse_code': "Use '.' for dots and '-' for dashes. E.g., '.-'",
            'character': "Enter a single uppercase letter or digit. E.g., 'A'",
        }
        widgets = {
            'character': forms.TextInput(attrs={'style': 'text-transform: uppercase;'}),
        }

    def clean_character(self):
        character = self.cleaned_data['character']
        return character.upper()