# frozen_string_literal: true

require 'json'
require 'awesome_print'

class Object
  def to_py
    JSON.dump(self)
  end
end

class TrueClass
  def to_py
    'True'
  end
end

class FalseClass
  def to_py
    'False'
  end
end

class NilClass
  def to_py
    'None'
  end
end

class Hash
  def to_py
    out = []
    each_pair { |key, value| out << "#{key.to_py}: #{value.to_py}" }
    "{ #{out.join("\n")} }"
  end
end

def allcommands(data)
  allcommands = []
  data.each_value { |val| allcommands += val }
  allcommands
end

def contexts(data)
  non_unique_contexts = allcommands(data).map { |cmd| cmd['context'] }
  non_unique_contexts.uniq
end

def space_type(data, contextname)
  allcommands(data).find { |cmd| cmd['context'] == contextname }['space_type']
end

def region_type(data, contextname)
  allcommands(data).find { |cmd| cmd['context'] == contextname }['region_type']
end

def entries_in_context(data, contextname)
end
