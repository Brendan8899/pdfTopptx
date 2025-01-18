import interpreter
import assembler


contentObjectList = interpreter.interpretMain("test/hacknrollSimple.pdf")
assembler.assemble(contentObjectList,"output.pptx")

