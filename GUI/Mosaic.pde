color c;
PImage img;
PFont font;
PFont font1;
boolean rectOver;
int rectX;
int rectY;
int rectWidth;
int rectHeight;

void setup() {
  size(500, 375);
  //smooth(4);
  pixelDensity(displayDensity());
  rectWidth = 200;
  rectHeight = 80;
  background(55);  
  img = loadImage("banner.png");
  image(img, 0, 10, width, width/2.4);
  fill(255);
  font = loadFont("Pixellari-250.vlw");
  textFont(font, 40);
  text("For Lego Digital Designer", 25, 200);
  rectOver = false;
}

void draw() {
  update();
  if (rectOver) {
      fill(28,66,142);
    } else {
      fill(30,91,215);
    }
    noStroke();
    rectX = width/2-rectWidth/2;
    rectY = height/2-rectHeight/2+100;
    rect(rectX, rectY, rectWidth, rectHeight, 4);
    
    if (rectOver){
      fill(225);  
    } else{
     fill(255); 
    }
    font = loadFont("Pixellari-250.vlw");
    textFont(font, 28);
    text("Select Image", 170, 296);
}

void mousePressed() {
  if (rectOver) {
    print("CLICK!");
    //exec("bash launch"); 
    launch("/Applications/main.app");
    //selectInput("Select a file to process:", "fileSelected");
    fill(255,255,255);
  }
}

void update() {
  if( overRect(rectX, rectY, rectWidth, rectHeight) ) 
  {
    rectOver = true;
  } 
  else 
  {
    rectOver = false;
  }
}

boolean overRect(int x, int y, int width, int height)  {
  if (mouseX >= x && mouseX <= x+width && 
      mouseY >= y && mouseY <= y+height) {
    return true;
  } else {
    return false;
  }
}

void fileSelected(File selection) {
  if (selection == null) {
    println("Window was closed or the user hit cancel.");
  } else {
    println("User selected " + selection.getAbsolutePath());
  }
}