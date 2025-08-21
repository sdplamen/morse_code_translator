from rest_framework import serializers
from decoder.models import MorseMapping


class MorseMappingSerializer(serializers.ModelSerializer) :
    class Meta :
        model = MorseMapping
        fields = '__all__'
        extra_kwargs = {
            'character' :{'help_text' :'A single uppercase character (A-Z, 0-9)'},
            'morse_code' :{'help_text' :'Morse code sequence (e.g., .- for A)'},
        }