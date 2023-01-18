# from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import NoteSerializer
from .models import Note

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/notes/',
            'Method': 'GET',
            'Body': None,
            'description':'returns an array of notes',
        },
          {
            'Endpoint': '/notes/id',
            'Method': 'GET',
            'Body': None,
            'description':'returns a single note object',
        },
          {
            'Endpoint': '/notes/create',
            'Method': 'POST',
            'Body': {'body':""},
            'description':'creates a new note with data sent in the new req',
        },
          {
            'Endpoint': '/notes/id/update',
            'Method': 'PUT',
            'Body': {'body':""},
            'description':'updates existing note specific to id',
        },
          {
            'Endpoint': '/notes/id/delete',
            'Method': 'DELETE',
            'Body': None,
            'description':'deletes an existing note',
        }
    ]
    return Response(routes)

# get all notes 
@api_view(['GET'])
def getNotes(request):
        notes = Note.objects.all()
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)

# get note by id
@api_view(['GET'])
def getNote(request, pk):
        note = Note.objects.get(id=pk)
        serializer = NoteSerializer(note, many=False)
        return Response(serializer.data)

# create note
@api_view(['POST'])
def CreateNote(request):
    data = request.data

    note = Note.objects.create(
       body = data['body'] 
    ) 
    
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)

# update note
@api_view(['PUT'])
def updateNote(request, pk):
    data = request.data

    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)    

# delete note
@api_view(['DELETE'])
def deleteNote(request, pk):
   
    note = Note.objects.get(id=pk)
    note.delete()
    return Response('Note was deleted') 