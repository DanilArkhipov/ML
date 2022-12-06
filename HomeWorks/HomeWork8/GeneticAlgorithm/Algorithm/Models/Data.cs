using Newtonsoft.Json;

namespace GeneticAlgorithm.Algorithm.Models
{
	public class Data
	{
		[JsonProperty("points")]
		public List<Point> Points { get; set; }
		[JsonProperty("type")]
		public string Type { get; set; }
	}
}