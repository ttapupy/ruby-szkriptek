# encoding: UTF-8
# Fájl- és mappanév tisztító OneDrive szinkronizáláshoz
# A ( #~"#%&*:<>?\{|} ) és az esetleges láthatatlan karekterek cseréje ( _ )-ra
puts "Add meg az elérési útvonalat: "
osveny = gets.chomp
Dir.chdir("#{osveny}")


logall = "#{Dir.home}/atnevezes.txt"
$stdout = File.new( logall, 'a' )
$stdout.sync = true

puts
puts "#{Time.now}"
puts "Könyvtár: #{osveny}/"

karakterek = /[~\"#\$%&\*:<>\?\\{|}[^[:print:]]]/
tiszta = "_"

#könyvtárak

mappa = Array.new
mappaUj = Array.new

Dir.glob('**/*').each do |d|
  
  if File.directory? d 
      
    dv = d.split('/')[-1]
    if dv.match(karakterek) then
        mappa.push(d)
        ujAll = d.gsub (dv) do |match|
          match.gsub(karakterek, tiszta)
        end
        while File.exists?(ujAll)
            ujAll = "#{ujAll}_"
        end
        mappaUj.push(ujAll)        
    end
  end
end
 
for i in (0..mappa.count-1).to_a.reverse
  File.rename( mappa[i], mappaUj[i] )
  puts "Mappa átnevezve: #{mappa[i]}  --->>  #{mappaUj[i]}"
end  
    
Dir.chdir(Dir.home)

#állományok
puts

Dir.chdir("#{osveny}")

Dir.glob('**/*').select.each do |f|
  if File.file? f
    if f.match(karakterek) then
        ujAll = f.gsub(karakterek, tiszta)
        while File.exists?(ujAll)
            ujAll = "#{ujAll}_"
        end
        File.rename( f, ujAll )
        puts "Állomány átnevezve:  #{f}  --->  #{ujAll}"
    end
  end
end

puts " --- vége --- "
$stdout = STDOUT

puts "Módosítások itt: #{Dir.home}/atnevezes.txt"
puts
