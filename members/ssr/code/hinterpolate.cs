// If entry vCount[x,y] is true then it is counted in the next step.
// The last step is a column-wise longest vertical line counting
var vCount = new bool[with, height];
// Row major traversal
for (int y = 0; y < height; y++)
{
  // For each horizontal pixel interpolate with neighbours
  for (int x = windowSize; x < width - windowSize; x++)
  {
    double sum = 0d;
    // Horizontal average / interpolation,accepts slight slopes
    for (int k = -windowSize; k <= windowSize; k++)
      sum += srcFilter[x + k, y];
    double avg = sum / (2 * windowSize + 1);

    // Lowpass filter: If not really white then count it
    vCount[x, y] = avg < min_avg;
  }
}