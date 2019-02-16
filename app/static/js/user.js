function bookSearch() {
  var search = document.getElementById('search').value
  document.getElementById('results').innerHTML = ""
  console.log(search)
  $.ajax({
    url: "https://www.googleapis.com/books/v1/volumes?q=" + search +"&key=AIzaSyB9Q2aWWmNUHPG60ZK3RQczqe0mt_TAyHc",
    dataType: "json",
    success: function(books) {
      for (i = 0; i < books.items.length; i++) {
        results.innerHTML += "<h2>" + books.items[i].volumeInfo.title + "</h2>"
      }
      console.log(books)
    },
    type: 'GET'
  });
}