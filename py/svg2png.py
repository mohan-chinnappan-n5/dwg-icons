import argparse
import cairosvg

def convert_svg_to_png(input_svg, output_png):
    try:
        # Convert SVG to PNG using cairosvg
        cairosvg.svg2png(url=input_svg, write_to=output_png)

        print(f"Successfully converted SVG to PNG: {output_png}")

    except Exception as e:
        print(f"Error converting SVG to PNG: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert SVG file to PNG.')
    parser.add_argument('--input-svg', required=True, help='Input SVG file path')
    parser.add_argument('--output-png', required=True, help='Output PNG file path')
    args = parser.parse_args()

    convert_svg_to_png(args.input_svg, args.output_png)
