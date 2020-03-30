window.onload = init;


function init(){
  document.getElementById("currentPath").innerHTML = "No path found";
  eel.initialize();
}

eel.expose(checkPath);
function checkPath(data) { 
  if (data == ""){
    document.getElementById("currentPath").innerHTML = "No path found";
    pickFolder;
  }else{
    document.getElementById("currentPath").innerHTML = data.concat(" is the current path.");
    document.getElementById("data").value = data;
    eel.startApp();
  }
}

function pickFolder(){
  path = document.getElementById("data").value;
  eel.writePath(path);
  document.getElementById("currentPath").innerHTML = path.concat(" is the current path.");
  eel.startApp();
}