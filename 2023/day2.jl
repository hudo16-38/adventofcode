struct Game
    id::Int128
    records::Array{Dict{AbstractString, Int128}}
end

function parse_line(line::AbstractString)::Game
    game_info, records_info = split(line, ":")
    _, id = split(game_info, " ")
    id = parse(Int128, id)

    records = []
    records_info = strip(records_info)
    games = split(records_info, "; ")
    for game in games
        g = Dict("red" => 0, "blue" => 0, "green" => 0)
        colors = split(game, ", ")
        for color in colors
            count, name = split(color, " ")
            g[name] = parse(Int128, count)
        end
        push!(records, g)
    end
    return Game(id, records)
end

function parse_input(file_name::String)::Array{Game}
    file = open(file_name, "r")
    res = []
    for line in readlines(file)
        game = parse_line(strip(line))
        push!(res, game)
    end
    close(file)
    return res
end

function is_possible(game::Game, filter::Dict{String, Int})::Bool

    for record in game.records
        for color in keys(filter)
            if record[color] > filter[color]
                return false
            end
        end
    end
    return true
end

function filter_possible_games(games::Array{Game}, filter::Dict{String, Int})::Array{Game}
    res = []
    for game in games
        if is_possible(game, filter)
            push!(res, game)
        end
    end
    return res
end

function sum_ids(possible_games::Array{Game})::Int128
    return sum(game.id for game in possible_games)
end

function find_min_filter(game::Game)::Dict{String, Int128}
    filter = Dict("red" => 0, "green" => 0, "blue" => 0)

    for record in game.records
        for color in keys(record)
            filter[color] = max(filter[color], record[color])
        end
    end
    return filter
end

function set_power(filter::Dict{String, Int128})::Int128
    res = Int128(1)

    for value in values(filter)
        res *= value
    end
    return res
end
function sum_powers(games::Array{Game})::Int128
    s = Int128(0)

    for game in games
        min_filter = find_min_filter(game)
        p = set_power(min_filter)
        s += p
    end
    return s
end
const file_name = "inputs/day2.txt"
const filter = Dict("red" => 12, "green" => 13, "blue" => 14)
games = parse_input(file_name)
#println(games)
possible_games = filter_possible_games(games, filter)
#println(possible_games)
println(sum_ids(possible_games))
println(sum_powers(games))