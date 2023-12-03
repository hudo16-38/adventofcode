function replace_words(line::AbstractString)::String
    replacements = [
        ("one", "o1e"),
        ("two", "t2o"),
        ("three", "t3e"),
        ("four", "f4r"), 
        ("five", "f5e"),
        ("six", "s6x"),
        ("seven", "s7n"),
        ("eight", "e8t"),
        ("nine", "n9e")
    ]

    for (word, replacement) in replacements
        line = replace(line, word => replacement)
    end
    return line
end

function find_numbers(line::AbstractString, replace::Bool = false)::String
    if replace
        line = replace_words(line)
    end

    res = ""
    for char in line
        if isnumeric(char)
            res *= string(char)
        end
    end
    
    return res
end


function sum_numbers(file_name::String, replace::Bool = false)::Int128
    file = open(file_name, "r")
    s = 0

    for line in readlines(file)
        numbers = find_numbers(strip(line), replace)
        first = numbers[1]
        last = numbers[end]
        num = parse(Int128, first*last)
        s += num
    end
    close(file)
    return s
end

const file_name = "inputs/second_part.txt"
s = sum_numbers(file_name, true)
println(s)