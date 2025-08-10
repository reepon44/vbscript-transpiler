set dictionary = CreateObject("scripting.dictionary")

if dictionary.Exists("1") then
    dictionary("1") = dictionary("1") + 1
else
    dictionary("1") = 1
end if