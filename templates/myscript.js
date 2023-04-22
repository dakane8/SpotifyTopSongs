function logout() {
    // Send a request to the Spotify API to revoke the access token
    var xhr = new XMLHttpRequest();
    xhr.open('POST', 'https://accounts.spotify.com/api/token/revoke');
    xhr.setRequestHeader('Authorization', 'Bearer ' + access_token);
    xhr.send();
  
    // Clear the access token from the session storage
    sessionStorage.removeItem('access_token');
  
    // Redirect the user to the home page
    window.location.href = 'index.html';
  }