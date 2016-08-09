sum = 0;
sumN = 1;
var nextPageToken;

function getVids(PageToken){
    pid = $('#searchtext1').val();
    $.get(
        "https://www.googleapis.com/youtube/v3/playlistItems",{
        part : 'snippet', 
        maxResults : 50,
        playlistId : pid,
        pageToken : PageToken,
        key: 'YOUR API3 KEY'
        },
        function(data){
              myPlan(data);
        }        
    );  
 }

  function myPlan(data){
      total = data.pageInfo.totalResults;
      nextPageToken=data.nextPageToken;
      for(i=0;i<data.items.length;i++){
          document.getElementById('area1').value +=  
          sumN + '-' + data.items[i].snippet.title+'\n'+
          data.items[i].snippet.resourceId.videoId +'\n\n';
          sum++ ; sumN++;
          if(sum == (total-1) ){              
              sum = 0;  
              return;      
          }
      }  
      if(sum <(total-1)){
          getVids(nextPageToken);
      }    
 }
 
 function init(){
    $('#area1').val('');
 }