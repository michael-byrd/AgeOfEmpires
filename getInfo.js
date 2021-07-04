function Player(id, name, country, tg_rating,){
  this.id = id;
  this.name = '';
  this.country = '';
  this.tg_rating = 0;
  this.rating = 0;
}

var players = [];
var playerIDs = [];
var numPlayers = '';

// var country = '';
// var tg_rating = 0;
// var rating = 0;
function load() {
    var file = new XMLHttpRequest();
    file.open("GET", "info.txt", true);
    file.onreadystatechange = function() {
      if (file.readyState === 4) {  // Makes sure the document is ready to parse
        if (file.status === 200) {  // Makes sure it's found the file
          text = file.responseText;
          document.getElementById("div1").innerHTML = text;
        }
      }
    }
}

// function getInfo() {
//   var url = "https://aoe2.net/api/player/lastmatch?game=aoe2de&profile_id=313591";
//   var name = '123';
//   // $.getJSON(url, function(data) {
//   //         numPlayers = `${data.last_match.num_players}`;
//   //         for (let i = 0; i < numPlayers; i++){
//   //           playerIDs[i] = `${data.last_match.players[i].profile_id}`;
//   //         }
//   //         $(".mypanel").html(numPlayers);
//   //     });
//   $.ajax({ // gets the number of players and player ids and stores them
//     url: url,
//     async: false,
//     dataType: 'json',
//     success: function(data){
//       numPlayers = `${data.last_match.num_players}`;
//       // name = `${data.players[0].name}`;
//       for (let i = 0; i < numPlayers; i++){
//         playerIDs[i] = `${data.last_match.players[i].profile_id}`;
//       }
//     }
//     // $(".mypanel").html(playerIDs);
//   });



  // // for(i = 0; i < numPlayers; i++){
  //   var id = playerIDs[2];
  //   // // team game info
  //   url = 'https://aoe2.net/api/leaderboard?game=aoe2de&profile_id='+ 313591 +'&leaderboard_id=4';
  //   $.ajax({
  //     url: url,
  //     async: false,
  //     dataType: 'json',
  //     success: function(data){
  //       var name = `${data.total}`;
  //       // country = `${data.leaderboard.country}`;
  //       // tg_rating = `${data.leaderboard.rating}`;
  //
  //     }
  //     $(".mypanel").html(name);
  //   });
  // }



// }
