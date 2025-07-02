var mouseX = 0;
var mouseY = 0;
var sizeX = 0;
var sizeY = 0;
var docSizeY = 0;
var scrollTop = 0;
var scrollBottom = 0;

var productList = document.getElementById("productList");

function changePerspective(){
  if(mouseX==0&&mouseY==0){
    centreYperc = 100*((scrollTop + (sizeY/2))/docSizeY);
    mousePerc = 50;
  }else{   
    centreYperc = 100*((scrollTop + mouseY)/docSizeY);
    mousePerc = 100*(mouseX/sizeX);
  }  
  
  productList.style.perspectiveOrigin = mousePerc + "% " +   centreYperc + "%";
}


const { watchViewport } = tornis;

const updateValues = ({ size, scroll, mouse, orientation }) => {
  if (size.changed) {
    console.log("size");
    console.log(size);
    sizeX = size.x;
    sizeY = size.y;
    docSizeY = size.docY;
    changePerspective();
  }
  
  if (scroll.changed) {
    console.log("scroll");
    console.log(scroll);
    scrollTop = scroll.top;
    scrollBottom = scroll.bottom;
    changePerspective();
  }
 
  if (mouse.changed) {
    console.log("mouse");
    console.log(mouse);
    mouseX = mouse.x;
    mouseY = mouse.y;
    changePerspective();
  }
};

watchViewport(updateValues);