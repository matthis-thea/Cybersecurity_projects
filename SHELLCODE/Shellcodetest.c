// This is essential for test the bytecode

// echo 0 > /proc/sys/kernel/exec-shield   #turn it off
// echo 0 > /proc/sys/kernel/randomize_va_space #turn it off

// echo 1 > /proc/sys/kernel/exec-shield   #turn it on
// echo 1 > /proc/sys/kernel/randomize_va_space #turn it on

char code[] = "Put the bytecode here !!";
int main(int argc, char **argv)
{
  int (*func)();
  func = (int (*)()) code;
  (int)(*func)();
}

