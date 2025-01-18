import interpreter
import assembler


contentObjectList = interpreter.interpretMain("test/P5 CW Quesitons.pdf")
assembler.assemble(contentObjectList,"output.pptx")

