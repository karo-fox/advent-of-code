defmodule Part2 do
  @spec solve(String.t()) :: String.t()
  def solve(data), do:
  Regex.scan(~r/mul\((?<first>\d+),(?<second>\d+)\)/, sanitize(data))
    |> Enum.map(fn [_, first, second] -> [String.to_integer(first), String.to_integer(second)] end)
    |> Enum.map(fn [first, second] -> first*second end)
    |> Enum.sum()
    |> Integer.to_string()

  def sanitize(data), do:
    Regex.replace(~r/don't\(\).*$/,
      Regex.replace(~r/don't\(\).*do\(\)/U,
        data,
      ""),
    "")
end

data = File.read!("./2024/day03/input.txt")
result = Part2.solve(data)
IO.puts(result)
File.write!("./2024/day03/result2.txt", result)
