import interpreter
import transformer
import assembler
import config 

contentObjectList = interpreter.interpretMain(config.INPUT_FILENAME)
contentObjectList = transformer.transformMain(contentObjectList)

# for debug
# for c in contentObjectList:
#     if c["contentType"] == "text":
#         print(f"{c["pageNumber"]}::{c["content"][0:8]} ...")
        
assembler.assemble(contentObjectList, config.OUTPUT_FILENAME)

