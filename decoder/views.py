from django.shortcuts import render
from rest_framework import generics
from decoder.decoder_utils import MORSE_TO_CHAR_DICT, CHAR_TO_MORSE_DICT
from decoder.models import MorseMapping
from decoder.serializers import MorseMappingSerializer

def morse_decoder_view(request):
    decoded_message = ''

    if request.method == 'POST':
        morse_code_input = request.POST.get('morse_code', '').strip()

        if morse_code_input:
            words = morse_code_input.split(' | ')
            message_parts = []
            for word in words:
                letters = word.split(' ')
                # Use the imported dictionary
                norm_word = ''.join([MORSE_TO_CHAR_DICT.get(letter, '?') for letter in letters])
                message_parts.append(norm_word)
            decoded_message = ' '.join(message_parts)

    context = {
        'decoded_message': decoded_message,
        'prev_morse_input': request.POST.get('morse_code', ''),
    }
    return render(request, 'decoder.html', context)


def morse_encoder_view(request):
    encoded_message = ''
    if request.method == 'POST':
        english_input = request.POST.get('english_text', '').strip().upper()

        if english_input:
            encoded_words = []
            for word in english_input.split(' '):
                encoded_letters = []
                for char in word:
                    # Use the imported dictionary
                    encoded_letters.append(CHAR_TO_MORSE_DICT.get(char, '?'))
                encoded_words.append(' '.join(encoded_letters))
            encoded_message = ' | '.join(encoded_words)

    context = {
        'encoded_message': encoded_message,
        'prev_english_input': request.POST.get('english_text', ''),
    }
    return render(request, 'encoder.html', context)

class MorseMappingListCreate(generics.ListCreateAPIView):
    queryset = MorseMapping.objects.all()
    serializer_class = MorseMappingSerializer

class MorseMappingRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = MorseMapping.objects.all()
    serializer_class = MorseMappingSerializer
    lookup_field = 'pk'