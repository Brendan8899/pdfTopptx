import interpreter
import transformer
import assembler
import config 

contentObjectList = interpreter.interpretMain(config.INPUT_FILENAME)

contentObjectList = transformer.transformMain(contentObjectList)

assembler.assemble(contentObjectList, config.OUTPUT_FILENAME)

