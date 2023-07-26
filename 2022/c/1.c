#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
  FILE *f = fopen("../inputs/input1.txt", "r");
  if (!f) {
    fprintf(stderr, "Could not open file!\n");
    exit(0);
  }
  const size_t ln = 10;
  char line[ln];
  int ans = 0;
  int curr_sum = 0;
  int elves[4] = {0};

  while (fgets(line, ln, f)) {
    if (line[0] == '\n') {
      // for part 2
      elves[0] = curr_sum;

      size_t curr = 1;
      while (curr < 4 && elves[curr] < elves[curr - 1]) {
        int tmp = elves[curr - 1];
        elves[curr - 1] = elves[curr];
        elves[curr] = tmp;
        curr++;
      }

      // for part 1
      ans = ans > curr_sum ? ans : curr_sum;
      curr_sum = 0;
      continue;
    }

    char *num = strtok(line, "\n");
    curr_sum += atoi(num);
  }

  fclose(f);

  printf("part 1: %d\n", ans);

  printf("part 2: %d\n", elves[1] + elves[2] + elves[3]);

  return 0;
}
