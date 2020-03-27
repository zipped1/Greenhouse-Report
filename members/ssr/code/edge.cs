// theta is 0 for vertical edges, add some tolerance
var theta = Math.Atan2(pixel_y, pixel_x);
if (theta > -filterValues.ThetaTheshold && theta < filterValues.ThetaTheshold)
{
  var magnitude = Math.Ceiling(Math.Sqrt((pixel_x * pixel_x) + (pixel_y * pixel_y)));
  byte val = 0;
  if (magnitude < min_magnitude)
  {
    // Invert value: makes the image white instead of black
    val = (byte)(255 - magnitude);
  }
}