function deleteNote(noteID) {
    fetch('/delete-note', {
        method: 'POST',
        body: JSON.stringify({ noteId: noteId})
    }). then((_res) => {
        // refresh homepage
        window.location.href = "/";
    })
}