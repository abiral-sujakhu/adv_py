# wap that reads a large file in chunks and process using generator in python
"""
Program to read large files in chunks using generators
This approach is memory-efficient for processing large files
"""

def read_file_in_chunks(file_path, chunk_size=1024):
    """
    Generator function to read file in chunks
    
    Args:
        file_path: Path to the file to read
        chunk_size: Size of each chunk in bytes (default: 1024)
    
    Yields:
        Chunk of data from the file
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            yield chunk


def read_lines_in_batches(file_path, batch_size=100):
    """
    Generator function to read file line by line in batches
    
    Args:
        file_path: Path to the file to read
        batch_size: Number of lines per batch
    
    Yields:
        List of lines (batch)
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        batch = []
        for line in file:
            batch.append(line.strip())
            if len(batch) >= batch_size:
                yield batch
                batch = []
        
        # Yield remaining lines
        if batch:
            yield batch


def process_large_file(file_path, chunk_size=1024):
    """
    Process a large file using generator with character counting
    
    Args:
        file_path: Path to the file
        chunk_size: Size of each chunk
    
    Returns:
        Dictionary with processing statistics
    """
    total_chars = 0
    total_words = 0
    chunk_count = 0
    
    print(f"Processing file: {file_path}")
    print(f"Chunk size: {chunk_size} bytes\n")
    
    for chunk in read_file_in_chunks(file_path, chunk_size):
        chunk_count += 1
        total_chars += len(chunk)
        total_words += len(chunk.split())
        
        # Process each chunk (example: print first 50 chars)
        print(f"Chunk {chunk_count}: {chunk[:50]}...")
    
    return {
        'total_chunks': chunk_count,
        'total_characters': total_chars,
        'total_words': total_words
    }


def process_file_by_lines(file_path, batch_size=100):
    """
    Process file line by line using batch generator
    
    Args:
        file_path: Path to the file
        batch_size: Number of lines per batch
    
    Returns:
        Dictionary with processing statistics
    """
    total_lines = 0
    batch_count = 0
    
    print(f"\nProcessing file by lines: {file_path}")
    print(f"Batch size: {batch_size} lines\n")
    
    for batch in read_lines_in_batches(file_path, batch_size):
        batch_count += 1
        total_lines += len(batch)
        
        # Process each batch (example: print first line)
        if batch:
            print(f"Batch {batch_count}: Processing {len(batch)} lines. First line: {batch[0][:50]}...")
    
    return {
        'total_batches': batch_count,
        'total_lines': total_lines
    }


def create_sample_large_file(file_path, num_lines=1000):
    """
    Create a sample large file for testing
    
    Args:
        file_path: Path where the file will be created
        num_lines: Number of lines to generate
    """
    print(f"Creating sample file with {num_lines} lines...")
    
    with open(file_path, 'w', encoding='utf-8') as file:
        for i in range(num_lines):
            file.write(f"Line {i+1}: This is sample data for testing large file processing with generators. " * 5 + "\n")
    
    print(f"Sample file created: {file_path}\n")


# Advanced generator example: Filter and transform data
def process_and_filter_lines(file_path, filter_keyword=None):
    """
    Generator that reads, filters, and transforms lines
    
    Args:
        file_path: Path to the file
        filter_keyword: Keyword to filter lines (optional)
    
    Yields:
        Processed line that matches the filter
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        for line_num, line in enumerate(file, 1):
            line = line.strip()
            
            # Filter lines containing keyword
            if filter_keyword and filter_keyword.lower() not in line.lower():
                continue
            
            # Transform: add line number and uppercase
            yield f"[{line_num}] {line.upper()}"


def main():
    """Main function to demonstrate file processing with generators"""
    
    # Create a sample file
    sample_file = "sample_large_file.txt"
    create_sample_large_file(sample_file, num_lines=500)
    
    # Example 1: Read file in chunks
    print("=" * 60)
    print("EXAMPLE 1: Reading file in chunks")
    print("=" * 60)
    stats = process_large_file(sample_file, chunk_size=2048)
    print(f"\nStatistics:")
    print(f"  Total chunks: {stats['total_chunks']}")
    print(f"  Total characters: {stats['total_characters']}")
    print(f"  Total words: {stats['total_words']}")
    
    # Example 2: Read file line by line in batches
    print("\n" + "=" * 60)
    print("EXAMPLE 2: Reading file in line batches")
    print("=" * 60)
    stats = process_file_by_lines(sample_file, batch_size=50)
    print(f"\nStatistics:")
    print(f"  Total batches: {stats['total_batches']}")
    print(f"  Total lines: {stats['total_lines']}")
    
    # Example 3: Filter and process lines
    print("\n" + "=" * 60)
    print("EXAMPLE 3: Filtering and processing lines")
    print("=" * 60)
    print("Filtering lines containing 'Line 1':")
    count = 0
    for processed_line in process_and_filter_lines(sample_file, filter_keyword="Line 1"):
        if count < 5:  # Show only first 5 matches
            print(processed_line[:80] + "...")
            count += 1
    print(f"\n(Showing first 5 matches)")
    
    print("\n" + "=" * 60)
    print("All examples completed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()
