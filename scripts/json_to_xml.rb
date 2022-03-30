# frozen_string_literal: true

require 'json'

class Integer
  def to_xml(indent = 0)
    "<integer>#{self}</integer>\n".indent(indent)
  end
end

class Float
  def to_xml(indent=0)
    "<real>#{self}</real>\n".indent(indent)
  end
end

class String
  def to_xml(indent=0)
    "<string>#{self}</string>\n".indent(indent)
  end

  def indent(n)
    self.gsub(/^/, ' ' * n * 2)
  end
end

class FalseClass
  def to_xml(indent = 0)
    "<false/>\n".indent(indent)
  end
end

class TrueClass
  def to_xml(indent = 0)
    "<true/>\n".indent(indent)
  end
end

class Array
  def to_xml(indent = 0)
    return "<array/>\n".indent(indent) if self.empty?
    out = ["<array>\n"]
    self.each do |item|
      out << item.to_xml(1)
    end
    out << "</array>\n"
    out.join("").indent(indent)
  end
end

class Hash
  def to_xml(indent = 0)
    return "<dict/>\n".indent(indent) if self.empty?
    out = ["<dict>\n"]
    self.each do |k, v|
      out << "<key>#{k}</key>\n".indent(1)
      out << v.to_xml(1)
    end
    out << "</dict>\n"
    out.join("").indent(indent)
  end
end

puts JSON.parse(STDIN.read).to_xml
