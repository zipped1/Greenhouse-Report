var maxCol = new ColCounter { X = 0, Y = 0, Length = 0 };
// Column-wise longest line
for (int x = 0; x < w; x++)
{
  int colSum = 0;
  for (int y = 0; y < h; y++)
  {
    if (vCount[x, y])
      colSum++;
    else
      if (maxCol.Length < colSum)
      {
        maxCol.X = x;
        maxCol.Y = y - colSum;
        maxCol.Length = colSum;
      }
      colSum = 0;
  }
}
return maxCol;