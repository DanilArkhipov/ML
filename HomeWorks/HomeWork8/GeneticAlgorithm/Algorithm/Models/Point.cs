using Newtonsoft.Json;

namespace GeneticAlgorithm.Algorithm.Models
{
	public class Point
	{
		[JsonProperty("type")]
		public string Type { get; set; }
		[JsonProperty("x")]
		public double X { get; set; }
		[JsonProperty("y")]
		public double Y { get; set; }
	}
}