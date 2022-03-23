#define START_CHAR  'S'
#define END_CHAR    'P'
#define SEPERATOR   ','
#define NEW_LINE    '\n'
#define INTERVAL    50

#define RANDOM_MIN  0.0
#define RANDOM_MAX  1000.0
#define Y_VALUES    0
#define X_VALUES    1
#define TEST_DATA_SIZE  200

#define BANDRATE    115200

struct DATA_POINT{
  float x;
  float y;
  };

struct DATA_POINT dataset[TEST_DATA_SIZE];



DATA_POINT DATA_STRUCT_init(int i){
    DATA_POINT sample;
    sample.x = i;
    sample.y = random(0,200);
    return sample;
  }


void setup() {
  Serial.begin(BANDRATE); 
}

void loop(){
  for(int i =0; i < TEST_DATA_SIZE; i++){
    dataset[i] = DATA_STRUCT_init(i);
    }
  sendEvent(dataset);
  delay(INTERVAL);
}

void sendEvent(DATA_POINT sample[]) {
  Serial.print(START_CHAR + String(SEPERATOR));
  Serial.print(TEST_DATA_SIZE + String(SEPERATOR));
  writeFloat(sample, X_VALUES);
  writeFloat(sample, Y_VALUES);
  Serial.print(END_CHAR + String(SEPERATOR));
  Serial.print(NEW_LINE);
}

void writeFloat(DATA_POINT sample[] , int value){
  for (int i = 0; i < TEST_DATA_SIZE; i++){ 
    if(value == X_VALUES){Serial.print(sample[i].x); }
    else if(value == Y_VALUES){Serial.print(sample[i].y); }
    Serial.print(SEPERATOR);
    }
}
