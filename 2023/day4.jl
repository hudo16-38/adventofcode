using DataStructures

struct Card
    id::Int128
    my_numbers::Set{Int128}
    winnig_numbers::Set{Int128} 
end

function parse_line(line::AbstractString)::Card
    info, nums = split(line, ": ")
    _, id = split(info)
    id = parse(Int128, strip(id))

    my_nums, winning_nums = split(nums, " | ")
    my_nums = map(x -> parse(Int128, x), split(strip(my_nums)))
    winning_nums = map(x -> parse(Int128, x), split(strip(winning_nums)))

    return Card(id, Set(my_nums), Set(winning_nums))
end

function parse_input(file_name::String)::Array{Card}
    file = open(file_name, "r")

    res = []
    for line in readlines(file)
        card = parse_line(strip(line))
        push!(res, card)
    end
    close(file)
    return res
end

function count_winning_numbers(card::Card)::Int128
    common  = intersect(card.my_numbers, card.winnig_numbers)
    return length(common)  
end

function worth(card::Card)::Int128
    n = count_winning_numbers(card)
    if n == 0
        return 0
    end
    return 2^(n-1)
end

function worth_sum(cards::Array{Card})::Int128
    sum(worth(card) for card in cards)
end

function get_copies(card::Card)::Array{Int128}
    n = count_winning_numbers(card)
    return (card.id+1):(card.id+n)
end

function count_cards(cards::Array{Card})::Int128
    q = Queue{Any}()
    n = length(cards)

    for card in cards
        enqueue!(q, card)
    end

    count::Int128 = 0

    while !(isempty(q))
        card = dequeue!(q)
        count += 1
        copies = get_copies(card)

        for copy in copies
            for card in cards
                if card.id == copy
                    enqueue!(q, Card(copy, card.my_numbers, card.winnig_numbers))
                end
            end
        end
    end
    return count
end

const test_file = "inputs/day4.test.txt"
const file_name = "inputs/day4.txt"
cards = parse_input(file_name)
#println(cards)
w = worth_sum(cards)
println(w)
c = count_cards(cards)
println(c)