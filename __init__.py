import interpreter
import assembler


contentObjectList = interpreter.interpretMain("test/rust.pdf")

assembler.assemble(contentObjectList,"output.pptx")

