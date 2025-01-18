import interpreter
import assembler


contentObjectList = interpreter.interpretMain("test/HacknRoll.pdf")
assembler.assemble(contentObjectList,"output.pptx")

